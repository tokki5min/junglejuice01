const SECONDS = 12;
const RATE = 16000;
const btn = document.getElementById("btn");
const statusEl = document.getElementById("status");
const meter = document.getElementById("meter");
const note = document.getElementById("note");

function encodeWav(samples, rate) {
  const buf = new ArrayBuffer(44 + samples.length * 2);
  const v = new DataView(buf);
  const str = (o, s) => [...s].forEach((c, i) => v.setUint8(o + i, c.charCodeAt(0)));
  str(0, "RIFF"); v.setUint32(4, 36 + samples.length * 2, true); str(8, "WAVE");
  str(12, "fmt "); v.setUint32(16, 16, true); v.setUint16(20, 1, true); v.setUint16(22, 1, true);
  v.setUint32(24, rate, true); v.setUint32(28, rate * 2, true); v.setUint16(32, 2, true); v.setUint16(34, 16, true);
  str(36, "data"); v.setUint32(40, samples.length * 2, true);
  samples.forEach((s, i) => v.setInt16(44 + i * 2, Math.max(-1, Math.min(1, s)) * 0x7fff, true));
  return new Blob([buf], { type: "audio/wav" });
}

async function record() {
  const stream = await navigator.mediaDevices.getUserMedia({
    audio: { echoCancellation: false, noiseSuppression: false, autoGainControl: false },
  });
  const ctx = new AudioContext({ sampleRate: RATE });
  const src = ctx.createMediaStreamSource(stream);
  const chunks = [];
  await ctx.audioWorklet.addModule("/static/recorder-worklet.js");
  const node = new AudioWorkletNode(ctx, "recorder");
  node.port.onmessage = (e) => chunks.push(e.data);
  src.connect(node);
  await new Promise((r) => setTimeout(r, SECONDS * 1000));
  stream.getTracks().forEach((t) => t.stop());
  await ctx.close();
  const out = new Float32Array(chunks.reduce((n, c) => n + c.length, 0));
  let o = 0;
  for (const c of chunks) { out.set(c, o); o += c.length; }
  return encodeWav(out, RATE);
}

btn.onclick = async () => {
  btn.disabled = true; meter.textContent = ""; note.textContent = "";
  try {
    statusEl.textContent = `듣는 중... (${SECONDS}초)`;
    const wav = await record();
    statusEl.textContent = "분석 중...";
    const form = new FormData();
    form.append("audio", wav, "rec.wav");
    const res = await fetch("/api/analyze", { method: "POST", body: form });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail);
    meter.textContent = `AI 가능성 ${Math.round(data.ai_probability * 100)}%`;
    statusEl.textContent = `신뢰도: ${data.confidence === "low" ? "낮음" : "보통"}`;
    note.textContent = data.note;
  } catch (e) {
    statusEl.textContent = "오류: " + e.message;
  } finally {
    btn.disabled = false;
  }
};

import { NextRequest, NextResponse } from "next/server";
export async function POST(req: NextRequest) {
  try {
    const { resume, jobDescription, generateCoverLetter } = await req.json();
    if (!resume || !jobDescription) return NextResponse.json({ error: "Provide resume and job description" }, { status: 400 });
    const ak = process.env.DEEPSEEK_API_KEY;
    const instr = generateCoverLetter ? "\n\nAfter the resume, add COVER_LETTER_SEPARATOR then a professional cover letter." : "";
    const p = "You are a resume expert. Rewrite the resume to match the JD.\n\nJD:\n" + jobDescription + "\n\nResume:\n" + resume + "\n\nUse strong verbs, quantify achievements, match keywords, ATS-friendly. Stay honest." + instr;
    const r = await fetch("https://api.deepseek.com/v1/chat/completions", {
      method: "POST",
      headers: { "Content-Type": "application/json", "Authorization": "Bearer " + ak },
      body: JSON.stringify({ model: "deepseek-chat", messages: [{ role: "system", content: "You are a resume optimization expert." }, { role: "user", content: p }], max_tokens: 4096 }),
    });
    const d = await r.json();
    if (!r.ok) return NextResponse.json({ error: d.error?.message || "AI error" }, { status: 500 });
    return NextResponse.json({ result: d.choices[0].message.content });
  } catch (e) { return NextResponse.json({ error: "Server error" }, { status: 500 }); }
}
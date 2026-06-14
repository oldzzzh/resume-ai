import { NextRequest, NextResponse } from "next/server";
export async function POST(req: NextRequest) {
  try {
    const formData = await req.formData();
    const file = formData.get("file") as File;
    if (!file) return NextResponse.json({ error: "No file" }, { status: 400 });
    const buffer = Buffer.from(await file.arrayBuffer());
    const mammoth = await import("mammoth");
    const result = await mammoth.extractRawText({ buffer });
    return NextResponse.json({ text: result.value });
  } catch (e: any) {
    return NextResponse.json({ error: e.message }, { status: 500 });
  }
}
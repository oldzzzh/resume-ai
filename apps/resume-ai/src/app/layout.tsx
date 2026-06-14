 import type { Metadata } from "next";
 import "./globals.css";
 
 export const metadata: Metadata = {
   title: "ResumeAI - AI-Powered Resume Optimization",
   description: "Optimize your resume with AI. Land more interviews.",
 };
 
 export default function RootLayout({ children }: { children: React.ReactNode }) {
   return (
     <html lang="en">
       <body>{children}</body>
     </html>
   );
 }

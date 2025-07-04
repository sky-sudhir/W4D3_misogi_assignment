import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
// import { NavBar } from "../components/NavBar";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "RecommendMe - AI Product Recommendations",
  description: "Discover products you'll love with AI-powered recommendations",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        {/* <NavBar /> */}
        <main>{children}</main>
      </body>
    </html>
  );
}

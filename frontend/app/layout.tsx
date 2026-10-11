import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Market AI Trading India',
  description: 'AI-powered market analysis and trading dashboard',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

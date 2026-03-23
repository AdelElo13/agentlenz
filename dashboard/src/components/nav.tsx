"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const links = [
  { href: "/", label: "Overview" },
  { href: "/costs", label: "Costs" },
  { href: "/waste", label: "Waste" },
  { href: "/recommendations", label: "Recommendations" },
  { href: "/budgets", label: "Budgets" },
];

export function Nav() {
  const pathname = usePathname();

  return (
    <nav className="w-56 border-r border-zinc-800 bg-zinc-950 p-4 min-h-screen">
      <div className="mb-8">
        <h1 className="text-lg font-bold text-white">AgentLens</h1>
        <p className="text-xs text-zinc-500">Cost Optimization</p>
      </div>
      <ul className="space-y-1">
        {links.map((link) => (
          <li key={link.href}>
            <Link
              href={link.href}
              className={`block px-3 py-2 rounded text-sm ${
                pathname === link.href
                  ? "bg-zinc-800 text-white"
                  : "text-zinc-400 hover:text-white hover:bg-zinc-900"
              }`}
            >
              {link.label}
            </Link>
          </li>
        ))}
      </ul>
    </nav>
  );
}

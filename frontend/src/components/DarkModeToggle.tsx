import { useEffect, useState } from "react";

export default function DarkModeToggle() {
  const [dark, setDark] = useState(() => document.documentElement.classList.contains("dark"));

  useEffect(() => {
    document.documentElement.classList.toggle("dark", dark);
  }, [dark]);

  return (
    <button
      type="button"
      onClick={() => setDark(!dark)}
      className="text-sm px-3 py-1 rounded border border-gray-300 dark:border-gray-600"
    >
      {dark ? "☀️" : "🌙"}
    </button>
  );
}

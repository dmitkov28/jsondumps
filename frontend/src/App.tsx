import { lazy, Suspense, useState } from "react";
import News from "./components/News";
const Repos = lazy(() => import("./components/Repos"));
import ViewToggle from "./components/ViewToggle";
import type { Tab } from "./types";
import CurrentDate from "./components/CurrentDate";
import DarkModeToggle from "./components/DarkModeToggle";
import { Heading, Subheading } from "./components/Heading";

const news = [
  {
    id: "1",
    title: "React 20 Released",
    date: new Date("2026-05-01"),
    description: "Major performance improvements and new concurrent features.",
    tags: ["react", "frontend"],
  },
  {
    id: "2",
    title: "TypeScript 6.0 Announced",
    date: new Date("2026-04-28"),
    description: "Introduces pattern matching and improved type inference.",
    tags: ["typescript", "languages"],
  },
  {
    id: "3",
    title: "Vite 7 Now Available",
    date: new Date("2026-04-25"),
    description: "Faster builds with native Rust bundler integration.",
    tags: ["vite", "tooling"],
  },
];

const repos = [
  {
    id: "1",
    name: "facebook/react",
    stars: 230000,
    description: "A declarative, component-based UI library for the web.",
    tags: ["ui", "frontend"],
  },
  {
    id: "2",
    name: "vitejs/vite",
    stars: 72000,
    description: "Next generation frontend tooling with instant HMR.",
    tags: ["bundler", "tooling"],
  },
  {
    id: "3",
    name: "microsoft/typescript",
    stars: 105000,
    description:
      "TypeScript is a superset of JavaScript that compiles to clean JS.",
    tags: ["languages", "compiler"],
  },
];

function App() {
  const [tab, setTab] = useState<Tab>("news");

  return (
    <div className="p-8 w-full min-h-screen bg-white text-gray-900 dark:bg-gray-900 dark:text-gray-100">
      <div className="flex justify-between items-center mb-4">
        <Heading />
        <DarkModeToggle />
      </div>
      <Subheading />
      <section className="flex flex-col gap-y-4">
        <CurrentDate />
        <ViewToggle activeTab={tab} onToggle={setTab} />
        {tab === "news" ? (
          <News news={news} />
        ) : (
          <Suspense fallback={<p>Loading...</p>}>
            <Repos repos={repos} />
          </Suspense>
        )}
      </section>
    </div>
  );
}

export default App;

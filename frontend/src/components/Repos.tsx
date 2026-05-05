import type { GithubRepo } from "../types";
import { HoverCard } from "./HoverCard";

export default function Repos({ repos }: { repos: GithubRepo[] }) {
  return (
    <ul className="space-y-2">
      {repos.map((item) => (
        <li key={item.id} className="flex items-center gap-x-3">
          <HoverCard
            trigger={
              <span className="font-semibold cursor-pointer underline decoration-dotted">
                {item.name}
              </span>
            }
          >
            <p className="font-bold mb">{item.name}</p>
            <p className="text-xs text-gray-500 mb-1">
              ⭐ {item.stars.toLocaleString()}
            </p>
            <p>{item.description}</p>
          </HoverCard>
          <div className="flex gap-1 flex-wrap">
            {item.tags.map((tag) => (
              <span
                key={tag}
                className="px-2 py-0.5 bg-blue-100 text-blue-700 text-xs rounded-full"
              >
                {tag}
              </span>
            ))}
          </div>
        </li>
      ))}
    </ul>
  );
}

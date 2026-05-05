import type { NewsArticle } from "../types";
import { HoverCard } from "./HoverCard";

export default function News({ news }: { news: NewsArticle[] }) {
  return (
    <ul className="space-y-2">
      {news.map((item) => (
        <li key={item.id} className="flex items-center gap-x-3">
          <HoverCard
            trigger={
              <span className="font-semibold cursor-pointer underline decoration-dotted">
                {item.title}
              </span>
            }
          >
            <p className="font-bold mb-1">{item.title}</p>
            <p className="text-xs text-gray-500 mb-1">
              {item.date.toLocaleDateString()}
            </p>
            <p>{item.description}</p>
          </HoverCard>
          <div className="flex gap-1 mt-2 flex-wrap">
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

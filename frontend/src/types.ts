export type NewsArticle = {
  id: string;
  title: string;
  date: Date;
  description: string;
  tags: string[];
};

export type GithubRepo = {
  id: string;
  name: string;
  stars: number;
  description: string;
  tags: string[];
};
export type Tab = "news" | "repos";

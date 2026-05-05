import type { Tab } from "../types";

export default function ViewToggle({
  activeTab,
  onToggle,
}: {
  activeTab: Tab;
  onToggle: (tab: Tab) => void;
}) {
  return (
    <div className="flex gap-4 mb-6">
      <ButtonTab
        value="news"
        isActive={activeTab == "news"}
        onToggle={onToggle}
      />
      <ButtonTab
        value="repos"
        isActive={activeTab == "repos"}
        onToggle={onToggle}
      />
    </div>
  );
}

const ButtonTab = ({
  value,
  isActive,
  onToggle,
}: {
  value: Tab;
  isActive: boolean;
  onToggle: (value: Tab) => void;
}) => {
  return (
    <button
      type="button"
      onClick={() => onToggle(value)}
      className={`px-4 py-2 border-b-2 ${isActive ? "border-b-black dark:border-b-white" : "border-b-transparent"}`}
    >
      {value.toUpperCase()}
    </button>
  );
};

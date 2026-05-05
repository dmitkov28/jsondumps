export default function CurrentDate() {
  return (
    <p className="text-sm text-gray-400">
      {new Date().toLocaleDateString(undefined, { weekday: "long", year: "numeric", month: "long", day: "numeric" })}
    </p>
  );
}

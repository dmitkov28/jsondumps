import { useState, type ReactNode } from 'react'

export function HoverCard({ trigger, children }: { trigger: ReactNode; children: ReactNode }) {
  const [open, setOpen] = useState(false)

  return (
    <div className="relative inline-block" onMouseEnter={() => setOpen(true)} onMouseLeave={() => setOpen(false)}>
      {trigger}
      {open && (
        <div className="absolute z-10 top-full left-0 mt-2 w-64 p-3 rounded-lg border bg-white shadow-lg text-sm text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-200">
          {children}
        </div>
      )}
    </div>
  )
}

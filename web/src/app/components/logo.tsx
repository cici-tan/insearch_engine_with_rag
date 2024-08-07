import React, { FC } from "react";

export const Logo: FC = () => {
  return (
    <div className="flex gap-4 items-center justify-center cursor-default select-none relative">
      <div className="h-10 w-10">
        <svg viewBox="0 0 85 85" className="h-full w-full">
          <circle cx="42.5" cy="42.5" r="35" fill="#597D50" />
          <circle cx="42.5" cy="42.5" r="20" fill="#A5B867" />
        </svg>
      </div>
      <div className="text-center font-medium text-2xl md:text-3xl text-zinc-950 relative text-nowrap">
        AI Policy Search
      </div>
      <div className="transform scale-75 origin-left border items-center rounded-lg bg-gray-100 px-2 py-1 text-xs font-medium text-zinc-600">
        ZJU
      </div>
    </div>
  );
};

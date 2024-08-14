"use client";
import { Footer } from "@/app/components/footer";
import { Logo } from "@/app/components/logo";
import { PresetQuery } from "@/app/components/preset-query";
import { Search } from "@/app/components/search";
import React from "react";

export default function Home() {
  return (
    <div className="absolute inset-0 min-h-[500px] flex items-center justify-center">
      <div className="relative flex flex-col gap-8 px-4 -mt-24">
        <Logo></Logo>
        <Search></Search>
        <div className="flex gap-2 flex-wrap justify-center">
          <PresetQuery query="嘉善县有什么比较好的创业政策?"></PresetQuery>
          <PresetQuery query="刚毕业的大学生想创业有什么补贴?"></PresetQuery>
        </div>
        <Footer></Footer>
      </div>
    </div>
  );
}

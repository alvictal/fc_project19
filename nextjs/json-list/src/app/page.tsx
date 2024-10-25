import { Suspense } from "react";
import Image from "next/image";
import { BlogPostList } from "./components/BlogPostList";
import BlogPostSkeleton from "./components/BlogPostSkeleton";

export default function Home() {
  return (
    <main className="container mx-auto px-4 py-6 bg-yellow-200">
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
      <Suspense fallback={new Array(15).fill(null).map((_, index) => (
            <BlogPostSkeleton key={index} />
          ))}>
          <BlogPostList />
        </Suspense>
      </div>
    </main>
  );
}

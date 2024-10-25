import { Post } from "@/models";
import Link from "next/link";
import { BlogPost } from "./BlogPost";

export async function getBlogPosts(): Promise<Post[]> {
    const url = 'https://jsonplaceholder.typicode.com/posts';
    const response = await fetch(url, {
        cache: "no-cache",
    });
    return response.json();
}

export async function BlogPostList() {
    const blogPosts = await getBlogPosts();
    return blogPosts.length ? (
        blogPosts.map((bpost, key) => (
            <BlogPost 
                key={key}
                userId={bpost.userId}
                id={bpost.id}
                title={bpost.title}
                body={bpost.body}
            /> 
        ))
    ):(
    <div className="flex items-center justify-center w-full col-span-full">
        <p className="text-gray-600 text-xl font-semibold">
          Nenhum post encontrado
        </p>
      </div>
    );
}
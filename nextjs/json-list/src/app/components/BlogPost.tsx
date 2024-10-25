import Image from "next/image";

export type BlogPostProps = {
    userId: number;
    id: number;
    title: string;
    body: string;
};

export function BlogPost(props: BlogPostProps) {
    const {
        userId,
        id,
        title,
        body,
    } = props
    return(
        <div className="max-w-sm mx-auto bg-slate-100 shadow-lg rounded-lg overflow-hidden">
            <div className="p-4">
                <h2 className="text-xl font-bold text-gray-800">{title}</h2>
                <p className="text-gray-600 mt-2">{userId} - {id}</p>
                <p className="text-gray-700 mt-6">{body}</p>
            </div>
        </div>
    );
}
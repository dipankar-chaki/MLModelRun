import DefaultLayout from "@/layouts/default";
import { useQuery } from "@tanstack/react-query";

export default function IndexPage() {
	const { data, isLoading } = useQuery({
		queryKey: ["repos", "data"],
		queryFn: async () => {
			const res = await fetch("http://localhost:5174/");
			return res.json();
		},
		staleTime: 10 * 60 * 1000,
	});

	if (isLoading) {
		return <div>Loading...</div>;
	}

	return (
		<DefaultLayout>
			<code>{data.message}</code>
		</DefaultLayout>
	);
}

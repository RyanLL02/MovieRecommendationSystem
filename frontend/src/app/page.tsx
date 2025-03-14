export default async function Home() {
  const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

  let tasks = [];
  try {
    const res = await fetch(`${API_URL}/tasks`, { cache: "no-store" });
    if (!res.ok) {
      throw new Error("Failed to fetch tasks");
    }
    tasks = await res.json();
  } catch (error) {
    console.error("Error fetching tasks:", error);
  }

  return (
    <main>
      <h1 className="text-2xl font-bold">Task List</h1>
      <ul>
        {tasks.length > 0 ? (
          tasks.map((task: { id: number; title: string; description: string }) => (
            <li key={task.id} className="border p-2 my-2 rounded">
              <strong>{task.title}</strong>: {task.description}
            </li>
          ))
        ) : (
          <p>No tasks found.</p>
        )}
      </ul>
    </main>
  );
}

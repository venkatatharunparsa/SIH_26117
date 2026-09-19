"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { Workbench } from "@/components/Workbench";
import { loadWalkSession, type WalkSession } from "@/lib/constants";

export default function WalkPage() {
  const params = useParams();
  const router = useRouter();
  const taskId = String(params.taskId || "");
  const [session, setSession] = useState<WalkSession | null>(null);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    const s = loadWalkSession(taskId);
    if (!s) {
      router.replace("/");
      return;
    }
    setSession(s);
    setReady(true);
  }, [taskId, router]);

  if (!ready || !session) {
    return (
      <p className="hero-meta" style={{ padding: "2rem" }}>
        Loading walk…
      </p>
    );
  }

  return <Workbench session={session} />;
}

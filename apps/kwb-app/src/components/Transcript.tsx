import { Bot, Keyboard, Sparkles } from "lucide-react";
import type { StreamEntry } from "../lib/constants";
import { ToolBlock } from "./ToolBlock";

type Props = {
  entries: StreamEntry[];
};

export function Transcript({ entries }: Props) {
  const hasWork = entries.some(
    (e) =>
      e.kind === "user" ||
      e.kind === "assistant" ||
      e.kind === "tool" ||
      e.kind === "ask"
  );

  if (!hasWork) {
    return (
      <div className="transcript">
        <div className="empty-stream">
          <div className="empty-mark" aria-hidden>
            <Sparkles size={22} strokeWidth={1.5} />
          </div>
          <h3>Knowledge Work Bench</h3>
          <p>
            Chat with the local station model. Attach context when you need an
            inspection ladder. Empty <kbd>Enter</kbd> continues a structured
            step when the agent asks — Monitor is evidence only.
          </p>
          <ul className="empty-hints">
            <li>
              <Keyboard size={13} aria-hidden /> Enter send · Shift+Enter newline
            </li>
            <li>
              <Bot size={13} aria-hidden /> Agent mode + model in the bar above
            </li>
          </ul>
        </div>
      </div>
    );
  }

  return (
    <div className="transcript" role="log" aria-live="polite">
      {entries.map((e) => {
        if (e.kind === "system") {
          return (
            <div key={e.id} className="entry-system">
              {e.text}
            </div>
          );
        }
        if (e.kind === "user") {
          return (
            <div key={e.id} className="entry-user">
              <div className="label">You</div>
              {e.text}
            </div>
          );
        }
        if (e.kind === "assistant") {
          return (
            <div key={e.id} className="entry-assistant">
              <div className="label">
                <Bot size={11} strokeWidth={2} aria-hidden />
                Assistant{e.model ? ` · ${e.model}` : ""}
              </div>
              {e.text}
            </div>
          );
        }
        if (e.kind === "ask") {
          return (
            <div key={e.id} className="entry-ask" data-ask={e.askKind}>
              <div className="label">Needs your input</div>
              <div className="ask-prompt">{e.prompt}</div>
              {e.contextPreview ? (
                <pre className="ask-context">{e.contextPreview}</pre>
              ) : null}
              <div className="ask-hint">
                Enter to confirm · type to correct · Shift+Enter for newline
              </div>
            </div>
          );
        }
        return <ToolBlock key={e.id} entry={e} />;
      })}
    </div>
  );
}

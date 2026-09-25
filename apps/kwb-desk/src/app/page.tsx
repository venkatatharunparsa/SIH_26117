/** Banner if someone bypasses npm refuse via legacy:force-dev. */
export default function HomePage() {
  return (
    <main
      style={{
        minHeight: "100vh",
        display: "grid",
        placeItems: "center",
        padding: "2rem",
        background: "#0e1116",
        color: "#e8eaed",
        fontFamily: "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace",
      }}
    >
      <div style={{ maxWidth: 520, lineHeight: 1.5 }}>
        <p style={{ color: "#f87171", fontWeight: 700, letterSpacing: "0.04em" }}>
          REJECTED / LEGACY
        </p>
        <h1 style={{ fontSize: "1.35rem", margin: "0.75rem 0" }}>
          Do not demo this app
        </h1>
        <p style={{ opacity: 0.85 }}>
          Primary product is the Electron desk:
        </p>
        <pre
          style={{
            marginTop: "1rem",
            padding: "1rem",
            background: "#161b22",
            borderRadius: 6,
            overflow: "auto",
          }}
        >
          {`cd apps/kwb-app\nnpm run electron:dev`}
        </pre>
        <p style={{ marginTop: "1rem", opacity: 0.7, fontSize: "0.9rem" }}>
          See <code>apps/kwb-desk/LEGACY.md</code>
        </p>
      </div>
    </main>
  );
}

import type { NextConfig } from "next";
import path from "path";

const nextConfig: NextConfig = {
  // Avoid picking a parent lockfile outside the repo
  outputFileTracingRoot: path.join(__dirname),
};

export default nextConfig;

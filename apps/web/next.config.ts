import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Allows Next.js to transpile our internal workspace package on the fly,
  // since @repo/units ships raw TypeScript with no build step.
  transpilePackages: ["@repo/units"],
};

export default nextConfig;

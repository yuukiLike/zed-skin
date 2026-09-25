/**
 * GreenTree Contrast AAA · 绿树 / 高对比度
 * A small forest, with room for every branch.
 */

export interface Tree {
  name: string;
  height: number;
  evergreen: boolean;
  children: readonly Tree[];
}
export const forest: Tree = {
  name: "GreenTree",
  height: 24,
  evergreen: true,
  children: [
    { name: "Cedar", height: 18, evergreen: true, children: [] },
    { name: "Maple", height: 12, evergreen: false, children: [] },
  ],
};

// Comments stay readable, even on the selected line.
export function countTrees(tree: Tree): number {
  return (
    1 +
    tree.children.reduce((sum, child) => {
      return sum + countTrees(child);
    }, 0)
  );
}

export function describeTree(tree: Tree): string {
  if (tree.height <= 0) {
    throw new Error("A tree needs room to grow.");
  }

  const canopy = tree.evergreen ? "evergreen" : "deciduous";
  return `${tree.name} · ${tree.height}m · ${canopy}`;
}

console.log(describeTree(forest));
console.log(`Trees in the forest: ${countTrees(forest)}`);

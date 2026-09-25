// GreenTree — room for every branch.
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
  ],
};

export class Forest {
  constructor(private readonly root: Tree) {}

  count(tree: Tree = this.root): number {
    return 1 + tree.children.reduce(
      (total, child) => total + this.count(child), 0,
    );
  }

  describe(): string {
    const { name, height } = this.root;
    return `${name} grows ${height}m tall.`;
  }
}

const grove = new Forest(forest);
console.log(grove.describe(), grove.count());

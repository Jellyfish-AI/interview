export type Team = {
  id: string;
  name: string;
};

export type Issue = {
  id: string;
  title: string;
  team: Team;
};

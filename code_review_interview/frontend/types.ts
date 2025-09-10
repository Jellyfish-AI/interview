export type Team = {
  id: string;
  name: string;
};

export type Issue = {
  id: string;
  title: string;
  team: Team;
};

export type EngineerType = {
  key: string;
  label: string;
  color: string;
};

export type Person = {
  id: number;
  name: string;
  team: Team;
  engineerType: EngineerType;
};

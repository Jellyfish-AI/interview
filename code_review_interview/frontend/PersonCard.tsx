import React from 'react';

import { Person } from './types';

type PersonCardProps = {
  person: Person;
};

export const PersonCard: React.FC<PersonCardProps> = (props) => {
  return (
    <div style={{ marginTop: '24px' }}>
      <div>{props.person.name}</div>
      <div>Team: {props.person.team.name}</div>
    </div>
  );
};

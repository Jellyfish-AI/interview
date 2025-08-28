import React from 'react';
import { Person } from './PeoplePage';

type PersonCardProps = {
  person: Person;
};

export const PersonCard: React.FC<PersonCardProps> = (props) => {
  return (
    <div>
      <h2>{person.name}</h2>
      <p>{person.email}</p>
    </div>
  );
};

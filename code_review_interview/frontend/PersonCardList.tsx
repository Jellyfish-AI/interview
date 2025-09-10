import React from 'react';

import { PersonCard } from './PersonCard';
import { Person } from './types';

type PersonCardListProps = {
  people: Person[];
};

export const PersonCardList: React.FC<PersonCardListProps> = (props) => {
  return (
    <div>
      {props.people.map((person) => (
        <PersonCard key={person.name} person={person} />
      ))}
    </div>
  );
};

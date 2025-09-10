import React from 'react';

import { PersonCard } from './PersonCard';

type PersonCardListProps = {
  people: object[];
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

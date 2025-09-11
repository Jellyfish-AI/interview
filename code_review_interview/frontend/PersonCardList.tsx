import React from 'react';

import { PersonCard } from './PersonCard';

type PersonCardListProps = {
  people: any[];
};

export const PersonCardList: React.FC<PersonCardListProps> = (props) => {
  if (!props.people) {
    return 'Loading...';
  }

  return (
    <div>
      {props.people.map((person) => (
        <PersonCard key={person.name} person={person} />
      ))}
    </div>
  );
};

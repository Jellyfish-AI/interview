import React, { useEffect } from 'react';

import { PersonCard } from './PersonCard';

type PersonCardListProps = {
  people: any;
};

export const PersonCardList: React.FC<PersonCardListProps> = (props) => {
  useEffect(() => {
    props.people.sort((a, b) => a.name.localeCompare(b.name));
  }, [props.people]);

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

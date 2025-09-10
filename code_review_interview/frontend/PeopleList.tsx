import React, { useEffect } from 'react';

import { PeopleListCard } from './PeopleListCard';

type PeopleListProps = {
  people: any;
};

export const PeopleList: React.FC<PeopleListProps> = (props) => {
  useEffect(() => {
    props.people.sort((a, b) => a.name.localeCompare(b.name));
  }, [props.people]);

  if (!props.people) {
    return 'Loading...';
  }

  return (
    <div>
      {props.people.map((person) => (
        <PeopleListCard key={person.name} person={person} />
      ))}
    </div>
  );
};

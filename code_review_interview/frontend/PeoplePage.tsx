import React from 'react';
import { useQuery } from 'react-query';

export type Person = {
  id: string;
  name: string;
  email: string;
};

export const PeoplePage: React.FC = () => {
  const { data: people } = useQuery<Person[]>(['GET_PEOPLE'], () =>
    fetch('https://api.jellyfish.co/people', { method: 'GET' }).then((response) => response.json())
  );

  return (
    <div>
      <h1>People</h1>
      {people?.map((person) => (
        <PersonCard person={person} />
      ))}
    </div>
  );
};

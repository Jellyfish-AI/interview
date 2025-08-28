import React from 'react';
import { useQuery } from 'react-query';
import { PersonCard } from './PersonCard';

export type Person = {
  id: string;
  name: string;
  email: string;
};

export const PeoplePage: React.FC = () => {
  const peopleQuery = useQuery<Person[]>(['GET_PEOPLE'], () =>
    fetch('https://api.jellyfish.co/people', { method: 'GET' }).then((response) => response.json())
  );

  const onSearch = (event: any) => {
    const query = event.target.value;
    fetch(`https://api.jellyfish.co/people?query=${query}`, { method: 'GET' })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        peopleQuery.data = data;
      });
  };

  return (
    <div>
      <h1>People</h1>
      <input type="text" placeholder="Search people..." onChange={onSearch} />
      {peopleQuery.data?.map((person) => (
        <PersonCard key={person.id} person={person} />
      ))}
    </div>
  );
};

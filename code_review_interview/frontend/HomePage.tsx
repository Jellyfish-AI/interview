import React from 'react';
import { useQuery } from 'react-query';

import { IssueCardList } from './IssueCardList';
import { PersonCardList } from './PersonCardList';
import { Issue } from './types';

export const HomePage: React.FC = () => {
  const { data: issues } = useQuery<Issue[]>(
    ['GET_ISSUES'],
    () =>
      fetch('https://api.jellyfish.co/issues', { method: 'GET' }).then((response) =>
        response.json()
      ),
    { staleTime: 1_200_000 }
  );

  const { data: people } = useQuery(
    ['GET_PEOPLE'],
    () =>
      fetch('https://api.jellyfish.co/people', { method: 'GET' }).then((response) =>
        response.json()
      ),
    { staleTime: 1_200_000 }
  );

  return (
    <div>
      <h1>Issues</h1>
      <IssueCardList issues={issues} />

      <h1>People</h1>
      <PersonCardList people={people} />
    </div>
  );
};

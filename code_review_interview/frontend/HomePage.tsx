import React from 'react';
import { useQuery } from 'react-query';

import { IssueList } from './IssueList';
import { PeopleList } from './PeopleList';
import { Issue } from './types';

export const HomePage: React.FC = () => {
  const { data: issues } = useQuery<Issue[]>(
    ['GET_ISSUES'],
    () => fetch('/issues', { method: 'GET' }).then((response) => response.json()),
    { staleTime: 1_200_000 }
  );

  const { data: people } = useQuery(
    ['GET_PEOPLE'],
    () => fetch('/people', { method: 'GET' }).then((response) => response.json()),
    { staleTime: 1_200_000 }
  );

  return (
    <div>
      <h1>Issues</h1>
      <IssueList issues={issues} />

      <h1>People</h1>
      <PeopleList people={people} />
    </div>
  );
};

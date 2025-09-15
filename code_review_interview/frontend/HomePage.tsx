import React from 'react';
import { useQuery } from 'react-query';

import { IssueCardList } from './IssueCardList';
import { Issue } from './types';

export const HomePage: React.FC = () => {
  const { data: issues } = useQuery<Issue[]>(
    ['GET_ISSUES'],
    () => fetch('/issues', { method: 'GET' }).then((response) => response.json()),
    { staleTime: 1_200_000 }
  );

  return (
    <div>
      <h1>Issues</h1>
      <IssueCardList issues={issues} />
    </div>
  );
};

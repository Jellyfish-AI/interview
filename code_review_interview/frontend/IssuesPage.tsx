import React from 'react';
import { useQuery } from 'react-query';

import { IssueCardList } from './IssueCardList';
import { Issue } from './types';

export const IssuesPage: React.FC = () => {
  const { data: issues } = useQuery<Issue[]>(
    ['GET_ISSUES'],
    () =>
      fetch('https://api.jellyfish.co/issues', { method: 'GET' }).then((response) =>
        response.json()
      ),
    { staleTime: 1_200_000 }
  );

  return (
    <div>
      <h1>Issues</h1>
      <IssueCardList issues={issues} />
    </div>
  );
};

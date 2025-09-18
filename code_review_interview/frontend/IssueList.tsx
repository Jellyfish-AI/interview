import React from 'react';

import { IssueListCard } from './IssueListCard';
import { Issue } from './types';

type IssueListProps = {
  issues: Issue[] | undefined;
};

export const IssueList: React.FC<IssueListProps> = (props) => {
  if (!props.issues) {
    return 'Loading...';
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      {props.issues.map((issue) => (
        <IssueListCard key={issue.id} issue={issue} />
      ))}
    </div>
  );
};

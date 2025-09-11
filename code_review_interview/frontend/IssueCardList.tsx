import React from 'react';

import { IssueCard } from './IssueCard';
import { Issue } from './types';

type IssueCardListProps = {
  issues: Issue[] | undefined;
};

export const IssueCardList: React.FC<IssueCardListProps> = (props) => {
  if (!props.issues) {
    return 'Loading...';
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      {props.issues.map((issue) => (
        <IssueCard key={issue.id} issue={issue} />
      ))}
    </div>
  );
};

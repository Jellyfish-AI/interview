import React from 'react';
import { useNavigate } from 'react-router-dom';

import { Person } from './types';

type PersonCardProps = {
  person: Person;
};

export const PersonCard: React.FC<PersonCardProps> = (props) => {
  const navigate = useNavigate();

  return (
    <div style={{ marginTop: '24px' }} onClick={() => navigate(`/person/${props.person.id}`)}>
      <div>{props.person.name}</div>
      <div>Team: {props.person.team.name}</div>
    </div>
  );
};

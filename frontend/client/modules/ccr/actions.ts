import { Dispatch } from 'redux';
import types from './types';
import { CCRDraft } from 'types/ccr';

export function initializeForm(ccrId: number) {
  return {
    type: types.INITIALIZE_CCR_FORM_PENDING,
    payload: ccrId,
  };
}

export function updateCCRForm(form: Partial<CCRDraft>) {
  return (dispatch: Dispatch<any>) => {
    dispatch({
      type: types.UPDATE_CCR_FORM,
      payload: form,
    });
    dispatch(saveCCRDraft());
  };
}

export function saveCCRDraft() {
  return { type: types.SAVE_CCR_DRAFT_PENDING };
}

export function fetchCCRDrafts() {
  return { type: types.FETCH_CCR_DRAFTS_PENDING };
}

export function createCCRDraft() {
  return {
    type: types.CREATE_CCR_DRAFT_PENDING,
  };
}

export function fetchAndCreateCCRDrafts() {
  return {
    type: types.FETCH_AND_CREATE_CCR_DRAFTS,
  };
}

export function deleteCCRDraft(ccrId: number) {
  return {
    type: types.DELETE_CCR_DRAFT_PENDING,
    payload: ccrId,
  };
}

// export function submitProposal(form: ProposalDraft) {
//   return async (dispatch: Dispatch<any>) => {
//     dispatch({ type: types.SUBMIT_CCR_PROPOSAL_PENDING });
//     try {
//       await putProposal(form);
//       const res = await putProposalSubmitForApproval(form);
//       dispatch({
//         type: types.SUBMIT_CCR_PROPOSAL_FULFILLED,
//         payload: res.data,
//       });
//     } catch (err) {
//       dispatch({
//         type: types.SUBMIT_CCR_PROPOSAL_REJECTED,
//         payload: err.message || err.toString(),
//         error: true,
//       });
//     }
//   };
// }

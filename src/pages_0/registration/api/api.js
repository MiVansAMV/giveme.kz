import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
console.log(',,', process.env.baseURL);
export const authApi = createApi({
  reducerPath: 'authApi',
  baseQuery: fetchBaseQuery({
    baseUrl: process.env.baseURL,
  }),
  endpoints: (builder) => ({
    postRegister: builder.mutation({
      query: (data) => ({
        url: '/user/signup',
        method: 'POST',
        body: data,
      }),
    }),
  }),
});
export const { usePostRegisterMutation } = authApi;
Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  root "evaluations#index"
  resources :trainings, only: [:index, :new]
  resources :evaluations, only: :index
end

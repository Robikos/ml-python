class EvaluationsController < ApplicationController
  def index
  end

  def create
    data = evaluation_params[:data]
    redirect_to evaluations_path, notice: "Thanks! You've just evaluated #{data}"
  end

  private

  def evaluation_params
    params.permit(:data)
  end
end

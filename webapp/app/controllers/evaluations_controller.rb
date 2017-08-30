class EvaluationsController < ApplicationController
  def index
  end

  def create
    data = evaluation_params[:data]
    MessagesProducer.publish({ request: [data] }.to_json)

    redirect_to evaluations_path, notice: "Thanks! You've just evaluated #{data}"
  end

  private

  def evaluation_params
    params.permit(:data)
  end
end
